#!/usr/bin/env python3
"""
Free LLM Models Fetcher
Fetches free models from OpenRouter, SiliconFlow, and Zhipu AI APIs
"""

import json
import os
import requests
from datetime import datetime
from typing import Dict, List, Any

class ModelFetcher:
    def __init__(self):
        self.data_dir = "data"
        self.output_file = os.path.join(self.data_dir, "free_models.json")
        self.ensure_data_dir()
        
    def ensure_data_dir(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def fetch_openrouter_models(self) -> List[Dict[str, Any]]:
        """Fetch free models from OpenRouter API"""
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            print("Warning: OPENROUTER_API_KEY not found")
            return []
        
        try:
            url = "https://openrouter.ai/api/v1/models"
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            models = response.json().get("data", [])
            free_models = []
            
            for model in models:
                # Filter for free models
                if model.get("pricing", {}).get("prompt", "0") == "0" and \
                   model.get("pricing", {}).get("completion", "0") == "0":
                    free_models.append({
                        "provider": "OpenRouter",
                        "id": model.get("id"),
                        "name": model.get("name"),
                        "description": model.get("description", ""),
                        "context_length": model.get("context_length", 0),
                        "pricing": model.get("pricing", {}),
                        "top_provider": model.get("top_provider", {}),
                        "created_at": model.get("created_at")
                    })
            
            print(f"Found {len(free_models)} free models from OpenRouter")
            return free_models
            
        except Exception as e:
            print(f"Error fetching OpenRouter models: {e}")
            return []
    
    def fetch_siliconflow_models(self) -> List[Dict[str, Any]]:
        """Fetch free models from SiliconFlow API"""
        api_key = os.getenv("SILICONFLOW_API_KEY")
        if not api_key:
            print("Warning: SILICONFLOW_API_KEY not found")
            return []
        
        try:
            url = "https://api.siliconflow.cn/v1/models"
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            models = response.json().get("data", [])
            free_models = []
            
            for model in models:
                # SiliconFlow free models typically have specific naming patterns
                model_id = model.get("id", "")
                if any(keyword in model_id.lower() for keyword in ["free", "guest", "demo"]):
                    free_models.append({
                        "provider": "SiliconFlow",
                        "id": model.get("id"),
                        "name": model.get("id"),  # SiliconFlow uses ID as name
                        "description": f"Free model from SiliconFlow",
                        "context_length": model.get("max_context_length", 0),
                        "pricing": {"prompt": "0", "completion": "0"},
                        "object": model.get("object"),
                        "created": model.get("created")
                    })
            
            print(f"Found {len(free_models)} free models from SiliconFlow")
            return free_models
            
        except Exception as e:
            print(f"Error fetching SiliconFlow models: {e}")
            return []
    
    def fetch_zhipu_models(self) -> List[Dict[str, Any]]:
        """Fetch free models from Zhipu AI API"""
        api_key = os.getenv("ZHIPU_API_KEY")
        if not api_key:
            print("Warning: ZHIPU_API_KEY not found")
            return []
        
        try:
            url = "https://open.bigmodel.cn/api/paas/v4/models"
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            models = response.json().get("data", [])
            free_models = []
            
            for model in models:
                # Zhipu AI free models identification
                model_id = model.get("id", "")
                if "glm-4-flash" in model_id.lower():  # GLM-4-Flash is their free model
                    free_models.append({
                        "provider": "Zhipu AI",
                        "id": model.get("id"),
                        "name": model.get("id"),
                        "description": f"Free model from Zhipu AI",
                        "context_length": model.get("max_tokens", 0),
                        "pricing": {"prompt": "0", "completion": "0"},
                        "object": model.get("object"),
                        "created": model.get("created"),
                        "owned_by": model.get("owned_by")
                    })
            
            print(f"Found {len(free_models)} free models from Zhipu AI")
            return free_models
            
        except Exception as e:
            print(f"Error fetching Zhipu AI models: {e}")
            return []
    
    def save_models_data(self, all_models: List[Dict[str, Any]]):
        """Save models data to JSON file"""
        data = {
            "updated_at": datetime.now().isoformat(),
            "total_count": len(all_models),
            "models": all_models
        }
        
        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Saved {len(all_models)} free models to {self.output_file}")
    
    def run(self):
        """Main execution method"""
        print("Starting to fetch free models...")
        
        all_models = []
        
        # Fetch from all providers
        all_models.extend(self.fetch_openrouter_models())
        all_models.extend(self.fetch_siliconflow_models())
        all_models.extend(self.fetch_zhipu_models())
        
        # Sort models by provider and name
        all_models.sort(key=lambda x: (x["provider"], x["name"]))
        
        # Save to file
        self.save_models_data(all_models)
        
        print(f"Completed! Total free models: {len(all_models)}")

if __name__ == "__main__":
    fetcher = ModelFetcher()
    fetcher.run()

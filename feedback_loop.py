import logging
from typing import Dict, Any
from pathlib import Path
import json

logger = logging.getLogger(__name__)

class FeedbackLoop:
    """Handles the continuous feedback loop for improving monetization strategies."""
    
    def __init__(self):
        self.training_data = []
        self.save_interval = 1000
        self.data_path = Path('feedback_data.json')
        
    def record_outcome(self, action: Dict[str, Any], reward: float, outcome: Dict[str, Any]) -> None:
        """Records the outcomes of actions for future learning.
        
        Args:
            action: The action taken by the RL agent.
            reward: The reward received from taking the action.
            outcome: Additional outcome information.
        """
        data_point = {
            'action': action,
            'reward': reward,
            **outcome
        }
        self.training_data.append(data_point)
        
    def save_data(self) -> None:
        """Saves the collected training data to a file."""
        if len(self.training_data) == 0:
            logger.info("No data to save.")
            return
            
        with open(self.data_path, 'w') as f:
            json.dump(self.training_data, f)
            
    def load_data(self) -> None:
        """Loads previous training data for continued learning."""
        if not self.data_path.exists():
            logger.info("No existing data found.")
            return
            
        try:
            with open(self.data_path, 'r') as f:
                self.training_data = json.load(f)
        except Exception as e:
            logger.error(f"Error loading data: {e}")
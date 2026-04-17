"""
Configuration file for Smart Irrigation AI Agent
Customize these settings to match your specific needs
"""

# Crop Configuration
SUPPORTED_CROPS = {
    'Wheat': {
        'icon': '🌾',
        'water_need': 'Moderate',
        'season': 'Winter',
        'optimal_moisture_range': (30, 50),
        'optimal_temp_range': (15, 25),
        'optimal_humidity_range': (50, 70),
        'daily_water_mm': 4.5,
        'irrigation_method': 'Drip or Sprinkler'
    },
    'Maize': {
        'icon': '🌽',
        'water_need': 'Moderate-High',
        'season': 'Summer',
        'optimal_moisture_range': (35, 55),
        'optimal_temp_range': (20, 30),
        'optimal_humidity_range': (55, 75),
        'daily_water_mm': 5.5,
        'irrigation_method': 'Drip or Furrow'
    },
    'Rice': {
        'icon': '🌾',
        'water_need': 'High',
        'season': 'Monsoon',
        'optimal_moisture_range': (60, 85),
        'optimal_temp_range': (25, 35),
        'optimal_humidity_range': (70, 90),
        'daily_water_mm': 7.5,
        'irrigation_method': 'Flood Irrigation'
    },
    'Cotton': {
        'icon': '🌸',
        'water_need': 'Moderate',
        'season': 'Summer',
        'optimal_moisture_range': (25, 45),
        'optimal_temp_range': (25, 35),
        'optimal_humidity_range': (50, 70),
        'daily_water_mm': 5.0,
        'irrigation_method': 'Drip'
    },
    'Sugarcane': {
        'icon': '🎋',
        'water_need': 'High',
        'season': 'Year-round',
        'optimal_moisture_range': (40, 65),
        'optimal_temp_range': (25, 35),
        'optimal_humidity_range': (60, 80),
        'daily_water_mm': 6.5,
        'irrigation_method': 'Furrow or Drip'
    },
    'Potato': {
        'icon': '🥔',
        'water_need': 'Moderate',
        'season': 'Winter',
        'optimal_moisture_range': (35, 55),
        'optimal_temp_range': (15, 25),
        'optimal_humidity_range': (60, 75),
        'daily_water_mm': 4.0,
        'irrigation_method': 'Drip or Sprinkler'
    }
}

# Growth Stage Configuration
GROWTH_STAGES = {
    'early': {
        'days_range': (1, 30),
        'name': 'Early Growth Stage',
        'description': 'Seedling establishment phase',
        'water_multiplier': 0.8,
        'recommendation': 'Use light, frequent irrigation to establish roots'
    },
    'critical': {
        'days_range': (30, 90),
        'name': 'Critical Growth Period',
        'description': 'Vegetative and reproductive phase',
        'water_multiplier': 1.2,
        'recommendation': 'Ensure consistent moisture for optimal development'
    },
    'mature': {
        'days_range': (90, 200),
        'name': 'Mature Stage',
        'description': 'Ripening and harvest preparation',
        'water_multiplier': 0.9,
        'recommendation': 'Monitor closely and adjust based on crop-specific needs'
    }
}

# Soil Moisture Thresholds
MOISTURE_ZONES = {
    'critical': {
        'range': (0, 30),
        'color': '#fecaca',
        'label': '🔴 Critical',
        'action': 'Immediate irrigation required'
    },
    'low': {
        'range': (30, 50),
        'color': '#fde68a',
        'label': '🟡 Low',
        'action': 'Consider irrigation soon'
    },
    'optimal': {
        'range': (50, 70),
        'color': '#a7f3d0',
        'label': '🟢 Optimal',
        'action': 'Maintain current levels'
    },
    'high': {
        'range': (70, 100),
        'color': '#93c5fd',
        'label': '🔵 High',
        'action': 'Check drainage, avoid over-watering'
    }
}

# Weather Adjustment Factors
WEATHER_ADJUSTMENTS = {
    'high_temp_threshold': 30,  # °C
    'low_humidity_threshold': 50,  # %
    'high_temp_water_increase': 0.15,  # 15% increase
    'low_humidity_water_increase': 0.10,  # 10% increase
    'evaporation_factor': 1.2
}

# Model Configuration
MODEL_CONFIG = {
    'test_size': 0.2,
    'random_state': 42,
    'cv_folds': 5,
    'n_jobs': -1,  # Use all CPU cores
    'synthetic_data_samples': 5000
}

# Random Forest Hyperparameters
RF_PARAMS = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

# Gradient Boosting Hyperparameters
GB_PARAMS = {
    'n_estimators': 200,
    'learning_rate': 0.1,
    'max_depth': 5,
    'random_state': 42
}

# UI Configuration
UI_CONFIG = {
    'page_title': 'Smart Irrigation AI Agent',
    'page_icon': '🌾',
    'layout': 'wide',
    'primary_color': '#667eea',
    'secondary_color': '#764ba2',
    'success_color': '#10b981',
    'warning_color': '#f59e0b',
    'danger_color': '#ef4444'
}

# Confidence Thresholds
CONFIDENCE_LEVELS = {
    'high': 75,  # Above 75% is high confidence
    'moderate': 50,  # 50-75% is moderate confidence
    'low': 0  # Below 50% is low confidence
}

# Irrigation Recommendations
IRRIGATION_METHODS = {
    'drip': {
        'name': 'Drip Irrigation',
        'efficiency': 90,
        'description': 'Most water-efficient method, delivers water directly to roots',
        'best_for': ['Cotton', 'Potato', 'Wheat', 'Maize']
    },
    'sprinkler': {
        'name': 'Sprinkler Irrigation',
        'efficiency': 75,
        'description': 'Good for uniform coverage, moderate efficiency',
        'best_for': ['Wheat', 'Potato', 'Maize']
    },
    'furrow': {
        'name': 'Furrow Irrigation',
        'efficiency': 60,
        'description': 'Traditional method, suitable for row crops',
        'best_for': ['Maize', 'Sugarcane']
    },
    'flood': {
        'name': 'Flood Irrigation',
        'efficiency': 50,
        'description': 'Required for rice paddies, maintains standing water',
        'best_for': ['Rice']
    }
}

# File Paths
FILE_PATHS = {
    'model': 'model.pkl',
    'label_encoder': 'label_encoder.pkl',
    'feature_importance': 'feature_importance.pkl',
    'dataset': 'irrigation_dataset.csv'
}

# Feature Names
FEATURE_NAMES = ['CropType', 'CropDays', 'SoilMoisture', 'Temperature', 'Humidity']

# Alert Messages
ALERTS = {
    'high_temp': '🌡️ **High Temperature:** Consider irrigating in early morning or evening to reduce evaporation.',
    'low_humidity': '💨 **Low Humidity:** Increase irrigation amount by 10-15% due to higher evaporation.',
    'critical_moisture': '🔴 **Critical:** Soil moisture is very low. Immediate irrigation required.',
    'high_moisture': '⚠️ **Caution:** Soil moisture is high. Ensure proper drainage to prevent waterlogging.',
    'heat_alert': '🌡️ **Heat Alert:** High temperature detected. Monitor soil moisture more frequently.'
}

# Success Messages
SUCCESS_MESSAGES = {
    'water_saved': '💰 **Water Saved:** By following AI recommendations, you\'re conserving water and reducing costs!',
    'optimal_conditions': '✅ **Optimal Conditions:** Your crop is in ideal growing conditions.',
    'good_decision': '🎯 **Smart Decision:** Following this recommendation will optimize crop health.'
}

# Export all configurations
__all__ = [
    'SUPPORTED_CROPS',
    'GROWTH_STAGES',
    'MOISTURE_ZONES',
    'WEATHER_ADJUSTMENTS',
    'MODEL_CONFIG',
    'RF_PARAMS',
    'GB_PARAMS',
    'UI_CONFIG',
    'CONFIDENCE_LEVELS',
    'IRRIGATION_METHODS',
    'FILE_PATHS',
    'FEATURE_NAMES',
    'ALERTS',
    'SUCCESS_MESSAGES'
]

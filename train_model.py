import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score, roc_auc_score
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

def generate_synthetic_data(n_samples=5000):
    """Generate realistic synthetic irrigation data"""
    np.random.seed(42)
    
    crops = ['Wheat', 'Maize', 'Rice', 'Cotton', 'Sugarcane', 'Potato']
    
    # Crop-specific parameters (optimal moisture ranges)
    crop_params = {
        'Wheat': {'moisture_range': (30, 50), 'temp_range': (15, 25), 'humidity_range': (50, 70)},
        'Maize': {'moisture_range': (35, 55), 'temp_range': (20, 30), 'humidity_range': (55, 75)},
        'Rice': {'moisture_range': (60, 85), 'temp_range': (25, 35), 'humidity_range': (70, 90)},
        'Cotton': {'moisture_range': (25, 45), 'temp_range': (25, 35), 'humidity_range': (50, 70)},
        'Sugarcane': {'moisture_range': (40, 65), 'temp_range': (25, 35), 'humidity_range': (60, 80)},
        'Potato': {'moisture_range': (35, 55), 'temp_range': (15, 25), 'humidity_range': (60, 75)}
    }
    
    data = []
    for _ in range(n_samples):
        crop = np.random.choice(crops)
        params = crop_params[crop]
        
        # Generate features with realistic distributions
        crop_days = np.random.randint(1, 150)
        soil_moisture = np.random.uniform(10, 95)
        temperature = np.random.normal(
            (params['temp_range'][0] + params['temp_range'][1]) / 2, 5
        )
        humidity = np.random.normal(
            (params['humidity_range'][0] + params['humidity_range'][1]) / 2, 10
        )
        
        # Smart irrigation logic
        moisture_threshold = params['moisture_range'][0]
        
        # Need irrigation if:
        # 1. Soil moisture is below threshold
        # 2. Temperature is high and humidity is low (evaporation)
        # 3. Crop is in critical growth stage (30-90 days)
        
        irrigation_score = 0
        
        if soil_moisture < moisture_threshold:
            irrigation_score += 3
        elif soil_moisture < moisture_threshold + 10:
            irrigation_score += 1
            
        if temperature > params['temp_range'][1] and humidity < params['humidity_range'][0]:
            irrigation_score += 2
            
        if 30 <= crop_days <= 90:  # Critical growth period
            irrigation_score += 1
            
        # Add some randomness for realism
        irrigation_score += np.random.uniform(-0.5, 0.5)
        
        irrigation = 1 if irrigation_score >= 2.5 else 0
        
        data.append({
            'CropType': crop,
            'CropDays': crop_days,
            'SoilMoisture': round(soil_moisture, 2),
            'temperature': round(temperature, 2),
            'Humidity': round(humidity, 2),
            'Irrigation': irrigation
        })
    
    return pd.DataFrame(data)

def train_advanced_model():
    """Train an advanced model with multiple gradient descent optimizers"""
    
    print("=" * 60)
    print("🌾 SMART IRRIGATION AI - ADVANCED GRADIENT DESCENT TRAINING")
    print("=" * 60)
    
    # Try to load existing dataset, otherwise generate synthetic data
    try:
        if os.path.exists("irrigation_dataset.csv"):
            print("\n📂 Loading existing dataset...")
            df = pd.read_csv("irrigation_dataset.csv")
        else:
            raise FileNotFoundError
    except:
        print("\n🔧 Generating synthetic irrigation dataset...")
        df = generate_synthetic_data(n_samples=10000)  # Increased to 10000 samples
        df.to_csv("irrigation_dataset.csv", index=False)
        print(f"✅ Generated {len(df)} samples and saved to 'irrigation_dataset.csv'")
    
    print(f"\n📊 Dataset shape: {df.shape}")
    print(f"📊 Irrigation distribution:\n{df['Irrigation'].value_counts()}")
    
    # Encode CropType
    le = LabelEncoder()
    df['CropType_encoded'] = le.fit_transform(df['CropType'])
    
    # Prepare features
    X = df[['CropType_encoded', 'CropDays', 'SoilMoisture', 'temperature', 'Humidity']]
    y = df['Irrigation']
    
    # Feature Scaling (Important for Gradient Descent!)
    print("\n🔧 Applying feature scaling for gradient descent optimization...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    
    # Split data with stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print("\n🔍 Training set size:", len(X_train))
    print("🔍 Test set size:", len(X_test))
    
    # Train multiple models with gradient descent
    print("\n🤖 Training multiple gradient descent-based models...")
    
    models = {}
    
    # Model 1: Stochastic Gradient Descent (SGD) Classifier
    print("\n1️⃣ Training SGD Classifier with optimal hyperparameters...")
    sgd_model = SGDClassifier(
        loss='log_loss',  # Logistic regression loss
        penalty='elasticnet',  # L1 + L2 regularization
        alpha=0.0001,
        l1_ratio=0.15,
        max_iter=2000,
        tol=1e-4,
        learning_rate='optimal',
        eta0=0.01,
        random_state=42,
        n_jobs=-1,
        early_stopping=True,
        validation_fraction=0.1,
        n_iter_no_change=10
    )
    sgd_model.fit(X_train, y_train)
    sgd_score = sgd_model.score(X_test, y_test)
    models['SGD'] = (sgd_model, sgd_score)
    print(f"✅ SGD Classifier accuracy: {sgd_score:.4f}")
    
    # Model 2: Logistic Regression with Gradient Descent
    print("\n2️⃣ Training Logistic Regression with gradient descent...")
    lr_model = LogisticRegression(
        solver='saga',  # Supports L1, L2, and ElasticNet
        penalty='elasticnet',
        l1_ratio=0.5,
        C=1.0,
        max_iter=2000,
        tol=1e-4,
        random_state=42,
        n_jobs=-1
    )
    lr_model.fit(X_train, y_train)
    lr_score = lr_model.score(X_test, y_test)
    models['LogisticRegression'] = (lr_model, lr_score)
    print(f"✅ Logistic Regression accuracy: {lr_score:.4f}")
    
    # Model 3: Neural Network with Gradient Descent (Adam optimizer)
    print("\n3️⃣ Training Neural Network with Adam optimizer...")
    nn_model = MLPClassifier(
        hidden_layer_sizes=(128, 64, 32),  # 3 hidden layers
        activation='relu',
        solver='adam',  # Adam optimizer (advanced gradient descent)
        alpha=0.0001,  # L2 regularization
        batch_size=32,
        learning_rate='adaptive',
        learning_rate_init=0.001,
        max_iter=500,
        tol=1e-4,
        early_stopping=True,
        validation_fraction=0.1,
        n_iter_no_change=15,
        random_state=42
    )
    nn_model.fit(X_train, y_train)
    nn_score = nn_model.score(X_test, y_test)
    models['NeuralNetwork'] = (nn_model, nn_score)
    print(f"✅ Neural Network accuracy: {nn_score:.4f}")
    
    # Model 4: Gradient Boosting with optimized parameters
    print("\n4️⃣ Training Gradient Boosting (uses gradient descent internally)...")
    gb_model = GradientBoostingClassifier(
        n_estimators=300,
        learning_rate=0.05,  # Gradient descent learning rate
        max_depth=7,
        min_samples_split=5,
        min_samples_leaf=2,
        subsample=0.8,
        max_features='sqrt',
        random_state=42,
        validation_fraction=0.1,
        n_iter_no_change=15,
        tol=1e-4
    )
    gb_model.fit(X_train, y_train)
    gb_score = gb_model.score(X_test, y_test)
    models['GradientBoosting'] = (gb_model, gb_score)
    print(f"✅ Gradient Boosting accuracy: {gb_score:.4f}")
    
    # Model 5: Random Forest (for ensemble)
    print("\n5️⃣ Training Random Forest for ensemble...")
    rf_model = RandomForestClassifier(
        n_estimators=300,
        max_depth=20,
        min_samples_split=2,
        min_samples_leaf=1,
        max_features='sqrt',
        random_state=42,
        n_jobs=-1
    )
    rf_model.fit(X_train, y_train)
    rf_score = rf_model.score(X_test, y_test)
    models['RandomForest'] = (rf_model, rf_score)
    print(f"✅ Random Forest accuracy: {rf_score:.4f}")
    
    # Create Voting Ensemble (combines all models)
    print("\n6️⃣ Creating Voting Ensemble (combines all models)...")
    voting_model = VotingClassifier(
        estimators=[
            ('sgd', sgd_model),
            ('lr', lr_model),
            ('nn', nn_model),
            ('gb', gb_model),
            ('rf', rf_model)
        ],
        voting='soft',  # Use probability voting
        n_jobs=-1
    )
    voting_model.fit(X_train, y_train)
    voting_score = voting_model.score(X_test, y_test)
    models['VotingEnsemble'] = (voting_model, voting_score)
    print(f"✅ Voting Ensemble accuracy: {voting_score:.4f}")
    
    # Select best model
    best_model_name = max(models, key=lambda k: models[k][1])
    best_model, best_score = models[best_model_name]
    
    print(f"\n🏆 Best model: {best_model_name} with accuracy: {best_score:.4f}")
    
    # Evaluate on test set
    y_pred = best_model.predict(X_test)
    y_pred_proba = best_model.predict_proba(X_test)[:, 1] if hasattr(best_model, 'predict_proba') else None
    
    print("\n" + "=" * 60)
    print("📈 BEST MODEL PERFORMANCE METRICS")
    print("=" * 60)
    print(f"\n✅ Model: {best_model_name}")
    print(f"✅ Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"✅ F1 Score: {f1_score(y_test, y_pred):.4f}")
    if y_pred_proba is not None:
        print(f"✅ ROC-AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")
    
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['No Irrigation', 'Irrigation Needed']))
    
    print("\n📊 Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print(f"\nTrue Negatives: {cm[0][0]}, False Positives: {cm[0][1]}")
    print(f"False Negatives: {cm[1][0]}, True Positives: {cm[1][1]}")
    
    # Cross-validation score
    print("\n🔄 Performing 5-fold cross-validation...")
    cv_scores = cross_val_score(best_model, X_scaled, y, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42), scoring='accuracy', n_jobs=-1)
    print(f"✅ Cross-validation scores: {cv_scores}")
    print(f"✅ Mean CV accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
    
    # Feature importance (if available)
    if hasattr(best_model, 'feature_importances_'):
        print("\n🔍 Feature Importance:")
        feature_names = ['CropType', 'CropDays', 'SoilMoisture', 'Temperature', 'Humidity']
        importances = best_model.feature_importances_
        feature_importance_dict = dict(zip(feature_names, importances))
        for name, importance in sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True):
            print(f"  {name}: {importance:.4f}")
    elif best_model_name == 'VotingEnsemble':
        # Get feature importance from the gradient boosting model in ensemble
        print("\n🔍 Feature Importance (from Gradient Boosting in ensemble):")
        feature_names = ['CropType', 'CropDays', 'SoilMoisture', 'Temperature', 'Humidity']
        importances = gb_model.feature_importances_
        feature_importance_dict = dict(zip(feature_names, importances))
        for name, importance in sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True):
            print(f"  {name}: {importance:.4f}")
    else:
        # For linear models, use coefficients
        print("\n🔍 Feature Coefficients:")
        feature_names = ['CropType', 'CropDays', 'SoilMoisture', 'Temperature', 'Humidity']
        if hasattr(best_model, 'coef_'):
            coefficients = np.abs(best_model.coef_[0])
            feature_importance_dict = dict(zip(feature_names, coefficients))
            for name, coef in sorted(zip(feature_names, coefficients), key=lambda x: x[1], reverse=True):
                print(f"  {name}: {coef:.4f}")
        else:
            feature_importance_dict = None
    
    # Print all model scores
    print("\n" + "=" * 60)
    print("📊 ALL MODEL ACCURACIES")
    print("=" * 60)
    for model_name, (model, score) in sorted(models.items(), key=lambda x: x[1][1], reverse=True):
        print(f"{model_name:20s}: {score:.4f} ({score*100:.2f}%)")
    
    # Save model, scaler, encoder, and feature importance
    joblib.dump(best_model, 'model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    joblib.dump(le, 'label_encoder.pkl')
    if feature_importance_dict:
        joblib.dump(feature_importance_dict, 'feature_importance.pkl')
    
    print("\n" + "=" * 60)
    print("✅ Model, scaler, encoder, and feature importance saved!")
    print("=" * 60)
    print(f"\n🎯 Final Accuracy: {best_score*100:.2f}%")
    print(f"🏆 Best Model: {best_model_name}")
    print("\n🚀 Run the Streamlit app with: streamlit run app.py")
    
    return best_model, scaler, le, best_score

if __name__ == "__main__":
    train_advanced_model()
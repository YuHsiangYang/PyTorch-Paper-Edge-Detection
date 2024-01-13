# Training pipeline
1. ## Generate dataset
    Run ``GenerateData.py``

    **Training dataset:**
    - Training Images: `current directory/data/Training/Images`
    - Training labels: `current directory/data/Training/Labels`
    
    **Validation dataset:**
    - Validation (image): `current directory/data/Validation/Images`
    - Validation (Labels): `current directory/data/Validation/Labels`
2. ## Check the generated dataset.
    `ReadPoints.py`
3. ## Merge the csv points to MAT file
    `MergeToMAT.py` -- Marge the csv files to one MAT file for faster access

    `loadmat.py` -- Check the produced format
4. ## Train the model
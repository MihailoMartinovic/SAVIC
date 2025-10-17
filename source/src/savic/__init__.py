import os
import numpy as np
import urllib
import wget
import warnings
warnings.filterwarnings("ignore")

# ==========================================================
# Expected file sizes
# ==========================================================

file_sizes_models = {
    'GMM_C/GMM_C.png': 48100,
    'GMM_C/GMM_C_Brazil_4.png': 3594210,
    'GMM_C/GMM_C_covariances.npy': 1696,
    'GMM_C/GMM_C_means.npy': 352,
    'GMM_C/GMM_C_weights.npy': 160,
    'GMM_CA/GMM_CA.png': 64121,
    'GMM_CA/GMM_CA_Brazil_6.png': 1089962,
    'GMM_CA/GMM_CA_covariances.npy': 9536,
    'GMM_CA/GMM_CA_means.npy': 800,
    'GMM_CA/GMM_CA_weights.npy': 176,
    'GMM_CB/GMM_CB.png': 82851,
    'GMM_CB/GMM_CB_Brazil_8.png': 1196694,
    'GMM_CB/GMM_CB_covariances.npy': 12672,
    'GMM_CB/GMM_CB_means.npy': 1024,
    'GMM_CB/GMM_CB_weights.npy': 192,
    'GMM_CBA/GMM_CBA.png': 142428,
    'GMM_CBA/GMM_CBA_Brazil_14.png': 4463508,
    'GMM_CBA/GMM_CBA_Brazil_refined_12.png': 4009836,
    'GMM_CBA/GMM_CBA_covariances.npy': 40560,
    'GMM_CBA/GMM_CBA_means.npy': 2256,
    'GMM_CBA/GMM_CBA_refined.png': 113786,
    'GMM_CBA/GMM_CBA_weights.npy': 240,
    'xgbc_kca.json': 14293033,
    'xgbc_kca.png': 51725,
    'xgbc_kcb.json': 58960041,
    'xgbc_kcb.png': 76527,
    'xgbc_kcba.json': 16574099,
    'xgbc_kcba.png': 92406,
    'xgbc_sus_c.json': 1850667,
    'xgbc_sus_c.png': 40687,
    'xgbc_sus_ca.json': 11984789,
    'xgbc_sus_ca.png': 29898,
    'xgbc_sus_cb.json': 18950584,
    'xgbc_sus_cb.png': 38598,
    'xgbc_sus_cba.json': 30488776,
    'xgbc_sus_cba.png': 43568,
    'xgbr_c.json': 16387983,
    'xgbr_c.png': 91188,
    'xgbr_ca_c0_a1_k0.json': 45454962,
    'xgbr_ca_c0_a1_k0.png': 108944,
    'xgbr_ca_c1_a0_k0.json': 16626577,
    'xgbr_ca_c1_a0_k0.png': 92845,
    'xgbr_ca_c1_a1_k0.json': 12857830,
    'xgbr_ca_c1_a1_k0.png': 99268,
    'xgbr_ca_c1_a1_k1.json': 3712066,
    'xgbr_ca_c1_a1_k1.png': 118761,
    'xgbr_cba_c0_b0_a1.json': 75864632,
    'xgbr_cba_c0_b0_a1.png': 113565,
    'xgbr_cba_c0_b1_a0_k0.json': 26606376,
    'xgbr_cba_c0_b1_a0_k0.png': 92448,
    'xgbr_cba_c0_b1_a0_k1.json': 16586299,
    'xgbr_cba_c0_b1_a0_k1.png': 93464,
    'xgbr_cba_c0_b1_a1.json': 23243410,
    'xgbr_cba_c0_b1_a1.png': 106928,
    'xgbr_cba_c1_b0_a0.json': 50577428,
    'xgbr_cba_c1_b0_a0.png': 82779,
    'xgbr_cba_c1_b0_a1.json': 24188460,
    'xgbr_cba_c1_b0_a1.png': 106436,
    'xgbr_cba_c1_b1_a0.json': 62450387,
    'xgbr_cba_c1_b1_a0.png': 126609,
    'xgbr_cba_c1_b1_a1.json': 10690959,
    'xgbr_cba_c1_b1_a1.png': 115973,
    'xgbr_cb_c0_b1_k0.json': 49250105,
    'xgbr_cb_c0_b1_k0.png': 112469,
    'xgbr_cb_c0_b1_k1.json': 29677188,
    'xgbr_cb_c0_b1_k1.png': 94806,
    'xgbr_cb_c1_b0.json': 58917559,
    'xgbr_cb_c1_b0.png': 86685,
    'xgbr_cb_c1_b1.json': 72669964,
    'xgbr_cb_c1_b1.png': 143089,
}

file_sizes_tutorials = {
    'SAVIC_Examples.h5': 12748480,
    'SAVIC_readme.pdf': 2185385,
    'SAVIC_testing.ipynb': 10626,
    'Article_I_Statistical_Trends.pdf': 1430282,
    'Article_II_Classification_and_Multidimensional_Mapping.pdf': 1532918,
}

# ==========================================================
# Base URLs
# ==========================================================

BASE_URL_MODELS = "https://raw.githubusercontent.com/MihailoMartinovic/SAVIC/main/Output/ML/models/"
BASE_URL_TUTORIAL = "https://raw.githubusercontent.com/MihailoMartinovic/SAVIC/main/tutorial/"

# ==========================================================
# Local directories (relative to package location)
# ==========================================================

PACKAGE_ROOT = os.path.dirname(__file__)
LOCAL_DIR_MODELS = os.path.join(PACKAGE_ROOT, "Output", "ML", "models")
LOCAL_DIR_TUTORIAL = os.path.join(PACKAGE_ROOT, "tutorial")

# ==========================================================
# Utility function
# ==========================================================

def check_and_download_files(file_dict, base_url, local_base):
    for rel_path, expected_size in file_dict.items():
        local_path = os.path.join(local_base, rel_path)
        dir_name = os.path.dirname(local_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        # Determine download reason
        if not os.path.exists(local_path):
            reason = "missing"
        elif os.path.getsize(local_path) != expected_size:
            reason = "wrong size"
        else:
            continue  # correct size, skip silently

        # Remove wrong-size file first
        if os.path.exists(local_path):
            os.remove(local_path)

        if reason == "missing":
            print(f"Missing: {rel_path} — downloading...")
        else:
            print(f"Size mismatch for {rel_path} — re-downloading...")

        url = urllib.parse.urljoin(base_url, rel_path)
        try:
            wget.download(url, local_path)
            print(f"\nDownloaded: {rel_path}")
        except Exception as e:
            print(f"\nFailed to download {rel_path}: {e}")

# ==========================================================
# Run automatically on import
# ==========================================================

check_and_download_files(file_sizes_models, BASE_URL_MODELS, LOCAL_DIR_MODELS)
check_and_download_files(file_sizes_tutorials, BASE_URL_TUTORIAL, LOCAL_DIR_TUTORIAL)

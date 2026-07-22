from firedrake import *
from firedrake.__future__ import interpolate
from multistream_clean import run_multistream
from vp1d import run_2d_vlasov
import numpy as np
from params import P
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_parameter_sweep():
    """Run simulations across different M and T values"""
    
    # Define parameter ranges
    M_values = [10,12]
    T_values_smol = np.round(np.arange(0.1, 1.0, 0.1), 1)
    T_values_big = np.arange(1,11)
    
    logger.info(f"M values: {M_values}")
    logger.info(f"Small T values: {T_values_smol}")
    logger.info(f"Large T values: {T_values_big}")
    
    total_ms_runs = len(M_values) * (len(T_values_smol) + len(T_values_big))
    total_vlasov_runs = len(T_values_smol) + len(T_values_big)
    
    logger.info(f"Total multistream runs: {total_ms_runs}")
    logger.info(f"Total 2D Vlasov runs: {total_vlasov_runs}")
    
    # Run multistream simulations
    logger.info("Starting multistream simulations...")
    ms_count = 0
    
    for M in M_values:
        logger.info(f"Running multistream with M = {M}")
        
        # Small T values
        for T in T_values_smol:
            ms_count += 1
            logger.info(f"  Run {ms_count}/{total_ms_runs}: M={M}, T={T}")
            try:
                run_multistream(M, T)
                logger.info(f"  ✓ Completed M={M}, T={T}")
            except Exception as e:
                logger.error(f"  ✗ Failed M={M}, T={T}: {str(e)}")
                continue
        
        
        # Large T values
        # for T in T_values_big:
        #     ms_count += 1
        #     logger.info(f"  Run {ms_count}/{total_ms_runs}: M={M}, T={T}")
        #     try:
        #         run_multistream(M, T)
        #         logger.info(f"  ✓ Completed M={M}, T={T}")
        #     except Exception as e:
        #         logger.error(f"  ✗ Failed M={M}, T={T}: {str(e)}")
        #         continue
    
    logger.info("Multistream simulations completed!")
    
    # Run 2D Vlasov simulations
    logger.info("Starting 2D Vlasov simulations...")
    vlasov_count = 0
    
    # Small T values
    for T in T_values_smol:
        vlasov_count += 1
        logger.info(f"Run {vlasov_count}/{total_vlasov_runs}: 2D Vlasov T={T}")
        try:
            run_2d_vlasov(T)
            logger.info(f"✓ Completed 2D Vlasov T={T}")
        except Exception as e:
            logger.error(f"✗ Failed 2D Vlasov T={T}: {str(e)}")
            continue
     
    
    # Large T values
    # for T in T_values_big:
    #     vlasov_count += 1
    #     logger.info(f"Run {vlasov_count}/{total_vlasov_runs}: 2D Vlasov T={T}")
    #     try:
    #         run_2d_vlasov(T)
    #         logger.info(f"✓ Completed 2D Vlasov T={T}")
    #     except Exception as e:
    #         logger.error(f"✗ Failed 2D Vlasov T={T}: {str(e)}")
    #         continue
   
    logger.info("All simulations completed!")

def run_quick_test():
    """Run a quick test with just a few parameter combinations"""
    logger.info("Running quick test...")
    
    # Test parameters
    test_M_values = np.arange(2,10)
    test_T_values = np.arange(1,11)
    
    for M in test_M_values:
        for T in test_T_values:
            logger.info(f"Test: M={M}, T={T}")
            try:
                run_multistream(M, T)
                logger.info(f"✓ Multistream test passed: M={M}, T={T}")
            except Exception as e:
                logger.error(f"✗ Multistream test failed: M={M}, T={T}: {str(e)}")
    
    for T in test_T_values:
        logger.info(f"Test: 2D Vlasov T={T}")
        try:
            run_2d_vlasov(T)
            logger.info(f"✓ 2D Vlasov test passed: T={T}")
        except Exception as e:
            logger.error(f"✗ 2D Vlasov test failed: T={T}: {str(e)}")
    
    logger.info("Quick test completed!")

def cleanup_directories():
    """Clean up output directories before running"""
    dirs_to_clean = [
        'vtk_ms_init', 'vtk_ms_final', 'ms_init', 'ms_final',
        'vtk_vlasov_init', 'vtk_vlasov_final', 'vlasov_init', 'vlasov_final'
    ]
    
    for dirname in dirs_to_clean:
        if os.path.exists(dirname):
            import shutil
            shutil.rmtree(dirname)
            logger.info(f"Cleaned directory: {dirname}")

if __name__ == "__main__":
    # Uncomment the operation you want to perform:
    
    # Option 1: Run quick test (recommended first)
    #run_quick_test()
    
    # Option 2: Clean directories and run full parameter sweep
    #cleanup_directories()
    #run_parameter_sweep()
    
    # Option 3: Just run the full parameter sweep without cleanup
    run_parameter_sweep()
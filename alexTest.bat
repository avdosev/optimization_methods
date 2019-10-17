cd one_dimensional_optimization  
python -m unittest test.TestSingleVariableOptimization.test_fib -v
cd ../multidimensional_optimization
python -m unittest test.TestMultiVariableOptimization.test_coordinate_descense test.TestMultiVariableOptimization.test_hooke_jeeves -v

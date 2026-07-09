def test_required_libraries_are_installed():
    import matplotlib
    import numpy
    import pandas
    import seaborn

    assert numpy is not None
    assert pandas is not None
    assert matplotlib is not None
    assert seaborn is not None
import numpy as np

def f0(x: np.ndarray) -> np.ndarray:
    return x[0] - (-0.188*x[1]) #sub(X0, mul(-0.188, X1))


def f1(x: np.ndarray) -> np.ndarray: 
    return (0.867*x[0]) #mul(0.867, X0)


def f2(x: np.ndarray) -> np.ndarray: ...


def f3(x: np.ndarray) -> np.ndarray: ...


def f4(x: np.ndarray) -> np.ndarray: ...


def f5(x: np.ndarray) -> np.ndarray: ...


def f6(x: np.ndarray) -> np.ndarray: ...


def f7(x: np.ndarray) -> np.ndarray: ...


def f8(x: np.ndarray) -> np.ndarray: ...


__all__ = ['f0', 'f1', 'f2']
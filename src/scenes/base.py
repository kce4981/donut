import numpy as np

class Base:
    vertices: np.array
    edges: list

    def __init__(self) -> None:
        self.dump = False
        self.payload = []

        pass


    def tick(self) -> None:
        pass

    def quit(self):
        if self.dump is True:
            self.__dumping()
    
    def __dumping(self) -> None:
        import pickle
        from pathlib import Path
        dump_path = Path(__file__).parents[2] / 'dumps' / f'{self.__class__.__name__}.data'
        with open(dump_path, mode='wb') as fp:
            pickle.dump(self.payload, fp)

if __name__ == '__main__':
    test = Base()
    test.dump = True
    test.payload.append('Hello!')
    test.quit()

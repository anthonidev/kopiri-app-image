from multiprocessing import freeze_support
import src.view.interphase as interphase

if __name__ == '__main__':
    freeze_support()
    interphase.init()

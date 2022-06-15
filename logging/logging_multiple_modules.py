import logging
import mylib


def main():
    logging.basicConfig(filename='testapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.test_logging()
    logging.info('Finished')


if __name__ == '__main__':
    main()





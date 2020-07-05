import time
import random
import subprocess
from threading import Timer
from functools import partial


def _espeak(msg):
    # Speak slowly in a female english voice
    cmd = ["espeak", '-s130', '-ven+f5', msg]
    subprocess.run(cmd)


def _vocalize(response, responsetts=None, interval=0):
    # "Comparisons to singletons like None should always be done with is or
    # is not, never the equality operators." -PEP 8
    if responsetts is not None:
        response = responsetts
    Timer(interval=interval, function=_espeak, args=(response,)).start()


def _get_response(q):
    time.sleep(random.uniform(0.5, 2))
    response = '42'
    response = 'BOT: ' + response
    return response


def _handle_query(q):
    response = _get_response(q)
    print(response)
    _vocalize(response, interval=0)


def main():
    prompt = partial(input, 'U: ')
    # alternative to using partial: iter(lambda: input('U: '), 'q')
    for query in iter(prompt, 'q'):  # quits on input 'q'
        _handle_query(query)


if __name__ == '__main__':
    main()

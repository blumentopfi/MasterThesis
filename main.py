from time import sleep

from agent.state import State

if __name__ == '__main__':
    state = State()

    for i in range(0, 100):
        state.step()
        sleep(1)


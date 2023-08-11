from contextlib import contextmanager

class Resource:
    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f'Resource was opened with arguments: {args}')
        self.opened = True

    def close(self):
        print('Resource was closed')
        self.opened = False

    def __del__(self):
        if self.opened:
            print(f'Memory leak detected. Resource was not closed')

    def action(self):
        print('Action was performed')

@contextmanager
def open_resource(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(*args)
        yield resource # generator
    except Exception:
        raise
    finally:
        if resource:
            resource.close()


if __name__ == '__main__':
    with open_resource(1, 2, 3) as resource:
        resource.action()





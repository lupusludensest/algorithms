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

if __name__ == '__main__':
    resource = None
    try:
        resource = Resource()
        resource.open(1, 2, 3)
        resource.action()
        raise ValueError()
    except:
        raise
    finally:
        if resource:
            resource.close()



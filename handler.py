import time

class GameEventHandler:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """Add a new game event to the handler."""
        self.events.append(event)

    def process_events(self):
        """Process all events in FIFO order."""
        while self.events:
            event = self.events.pop(0)
            self.handle_event(event)

    def handle_event(self, event):
        """Handle a single game event based on its type."""
        if event['type'] == 'action':
            self.perform_action(event['data'])
        elif event['type'] == 'input':
            self.handle_input(event['data'])
        else:
            print("Unknown event type")

    def perform_action(self, action_data):
        print(f'Performing action: {action_data}')

    def handle_input(self, input_data):
        print(f'Handling input: {input_data}')
        time.sleep(0.035)  # Simulating input latency

# Example usage if needed:
# handler = GameEventHandler()
# handler.add_event({'type': 'action', 'data': 'jump'})
# handler.add_event({'type': 'input', 'data': 'move_left'})
# handler.process_events()
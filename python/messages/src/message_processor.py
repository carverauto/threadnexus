from .models import NATSMessage
from .cloudevents_processor import process_cloudevent


class MessageProcessor:
    def __init__(self, neo4j_adapter):
        self.neo4j_adapter = neo4j_adapter

    async def process_message(self, msg):
        print(f"Received a message: {msg.data.decode()}")
        try:
            # Parse the raw message data into a NATSMessage object
            message_data = NATSMessage.parse_raw(msg.data.decode())
            if self.neo4j_adapter is not None:
                await process_cloudevent(message_data, self.neo4j_adapter)
            else:
                print("Neo4j adapter not initialized.")
        except Exception as e:
            print(f"Error processing message: {e}")
            # Optionally, handle or log the error appropriately
        finally:
            # Correctly acknowledge the message in JetStream context
            await msg.ack()

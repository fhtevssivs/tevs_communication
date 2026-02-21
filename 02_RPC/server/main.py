from jsonrpcserver import method, serve, Success  # Import necessary tools from the jsonrpcserver package


# Define a JSON-RPC method called "add"
# The client can call this method by sending {"method": "add", "params": {"a": ..., "b": ...}}
@method
def add(a, b):
    # Return the sum of a and b, wrapped in a Success object (standard JSON-RPC response)
    return Success(a + b)


# This block runs only if the script is started directly (not imported as a module)
if __name__ == "__main__":
    print("Starting server...")

    # Start the server on port 2000 and wait for JSON-RPC requests over HTTP
    serve(port=2000)

# Server Side Programming

## 25/04/23

## Joe

# RPC APIs

> RPC stands for Remote Procedure Call

It is a technology used to create distributed programs client/server that provides a high level communication paradigm in the OS, presuming the existence of a transport protocol such as TCP/IP or UDP to carry the messages between programs.
In other words, the user can use remote procedures as if they were local calls, without having to worry about possible differences such as architecture of client and server's machines.

## How does it work?

It's similar to a local procedure call:

- Arguments are passed to the procedure via a specific local, such as a register;
- Control's then passed to the process;
- Eventually control's taken back to the process that fired the procedure and it's execution keeps going on.

RPC works similarly:

- First the client process sends a message containing procedure's params to the server and then awaits a response;
- Then, a server process - _which was inactive until now_ - extracts these params, compute the results and then send back a response to the client. After that the process goes back on waiting another call;
- When client process receives the response, it extracts the results from the message and resumes its execution.

According to this model, only one of the two - client and server processes - can be activated at time although the RPC protocol does not restrict the implementation of a concurrent model. _A implementation that creates a async procedure, allowing the client to keep its execution while awaits on the response of the server_

## gRPC

In gRPC, a client application can be called directly using a method in a server application in a different machine as if it was a local object, easing the creation of distributed applications and services;

> gRPC APIs have the advantage that they can be used in a environment of different programming languages. You can use a Java server with Python, Go or Ruby clients.
>
> > Google uses it a lot!

It is a **modern, high-performance open-source RPC structure** that can be executed in any environment

### Protocol Buffers

By default, gRPC uses _Protocol Buffers_

> Protocol Buffers provide a extendable neutral language and platform mechanism to serialize structured data in a compatible manner with prior and post versions;

It's like a JSON, but faster and smaller. And generates native language calls.
One can define it as they wish once, then one can use the generated source-code to easily write and read structured data.
Protocol Buffers combine language definition, - _that will be created in a .proto file_ -, the code that the _proto_ compiler generates to interact with data, specific languages execution time libraries and the data serialization format that are recorded in a file.

#### Quickstart

1. First step's to define the data structure to serialize into a proto file;
2. Protocol Buffer's data are structured as messages, where each message's a tiny logical register of information containing a series of name-value pairs called fields.
   1. Here's an example:
      1.
      ```python
      message Person{
          optional string name = 1;
          optional int32 id = 2;
          optional string email = 3;
      }
      ```
3. After specifying the data structure, one uses the compiler to generate the class that can access the data in one's preferred language;
4. Those classes provide simple accessors to each field, such as `name()` and `set_name()` as well as methods to serialize/analyze all data structure from pure bytes.

```java
Person john = Person.newBuild()
    .setId(1234)
    .setName("John Doe")
    .setEmail("jdoe@example.com")
    .build();

output = new FileOutputStream(args[0]);
john.writeTo(output);
```

---

One can define a gRPC service in common proto files, with RPC methods params and return types specified as protocol buffer messages:

```c++
// The greeter service defition
service Greeter {
    // Sends a greeting
    rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name
message HelloRequest {
    string name = 1;
}

// The response message containing the greetings
message HelloReply {
    string message = 1;
}
```

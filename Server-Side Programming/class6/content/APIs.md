# APIs

---

- API stands for Application Programming Interface;
- They are a bunch of rules/protocols and tools that let different applications communicate between themselves;

## REST APIs

> REpresentational State Transfer (REST)

**"REST is a architecture style that aims to ease the communication between systems by providing them with industry default patterns"**

Systems that are compatible with the REST architecture are called RESTful and are stateless

#### Detaching Client and Server sides

Following the REST architecture means that implementation of both client and server sides can be done independently meaning that changes done in the client side won't affect the operation on server or vice versa - as long as they keep exchanging the correct type of content.

### Statelessness

To be stateless means that the server does not need to know anything about the state of the client or vice-versa. Meaning that both can send and receive messages even without knowing previous context.

> This statelessness restriction is rather done through resources than via commands
>
> > Resources are Web's substantives - they describe any object, document or thing you need to store or send to other services

Since REST APIs interact through standard operations via resources they do not rely on interface implementations. Those restrictions help RESTful applications to obtain reliability, faster performances and scalability, as components that can be managed, att and reused without affecting the system as a whole even during system's operations.

### Client and Server Communication

In REST architectures, clients send requests to retrieve or modify resources and servers send responses to those requests
RESTful requests are mode of:

- an HTTP verb defining the operation to be executed;
- a header allowing the client to give infos about the request;
- a resource path;
- a message body containing optional data;

#### HTTP Verbs

There are 4 HTTP basic verbs we often use in requests to interact with system's resources:

- _GET_ - retrieve a specific resource (by id) ou a resource's collection;
- _POST_ - creates a new resource;
- _PUT_ - att a specific resource (by id);
- _DELETE_ - removes a specific resource (by id);

#### Heading and Params

It is on the heading of a request that the client specifies what kind of response it's awaiting on from the server. _Accept_'s the field name, it ensures that the server doesn't send data that the client cannot understand or process.
The content options are of the MIME Type.

> MIME stands for Multipurpose Internet Mail Extensions, containing a type and subtype divided by a /

for instance: text/html, text/css, text/plain...
image/png, image/jpeg, image/gif...
audio/wav, audio/mpeg...
video/mp4, video/ogg...
application/json, application/pdf, application/xml...

#### Paths

Conventionally the first part of the path should be the plural of the resource, maintaining paths simple and easy to understand. The path **fashionboutique.com/customers/223/orders/12** is crystal clear on what it's requesting because it's descriptive and hierarchical: it wants the 12th order of the 223rd customers.

#### Responses

**Content Types**
In the cases where the server's sending a payload to the client, it must include a content-type at the header. This header alerts the client about what kind of content's being sent throughout the body. These contents are also MIME Types and must be one of the types the client has specified in their accept field.

#### Response Codes

Along side with the response itself the server also sends a status code to warn the client infos about the success - or not - of the operation. As a developer it isn't necessary to know all status codes, but you should know the most commonly used ones.

- _GET_ return **200 (OK)**
- _POST_ return **201 (CREATED)**
- _PUT_ return **200 (OK)**
- _DELETE_ return **204 (NO CONTENT)**

  If the operation fails, it'd be wise to return the most specific code possible accordingly to the problem

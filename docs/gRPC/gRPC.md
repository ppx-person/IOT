# gPRC https://grpc.io/
* A high perrformance,open source universal RPC framework
* protocol buffers
* gRPC can use protocal buffers as both its Interface Definition Language(IDL)
and as its underlying message interchange format.

```
message Person {
	string name = 1;
	int32 id = 2;
	bool has_ponycopter = 3;
}
```

```
service Greeter {
	// Sends a greeting
	rpc SayHello (HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
	string name = 1;
}

messag4e HelloReploy {
	string message = 1;
}
```


 

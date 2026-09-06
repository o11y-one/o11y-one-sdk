module github.com/o11y-one/o11y-one-sdk/tools/ci-runner

go 1.27

require (
	connectrpc.com/connect v1.20.0
	github.com/o11y-one/o11y-one-sdk/gen/go v0.0.0
	google.golang.org/protobuf v1.36.12
)

replace github.com/o11y-one/o11y-one-sdk/gen/go => ../../gen/go

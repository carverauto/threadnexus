// Package messages ./pkg/ports/messages/messages.go
package messages

// MessageAdapter is an interface for connecting to various message sources and listening for messages.
type MessageAdapter interface {
	Connect() error
	Listen(onMessage func(msg string))
}

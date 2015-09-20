FROM golang
#RUN go get github.com/aonx/axone
RUN CGO_ENABLED=0 go get -a -ldflags '-s' github.com/aonx/axone/...
RUN ls -lR /go/bin
ENTRYPOINT /go/bin/cmd start -c /go/src/github.com/aonx/axone/config.toml
EXPOSE 1883 7780

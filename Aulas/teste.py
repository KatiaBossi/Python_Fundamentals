from flask import Flask, escape, request

app=Flask (_name_)

@app.route('/')
def Hello ():
    name=request.args.get("name","worl")
    return 'hello, {escape(name)}'
extern crate ws;
extern crate env_logger;

fn main () {
    env_logger::init().unwrap();

    match ws::listen("127.0.0.1:3333", |out| {
        move |msg| {
            out.send(msg)
        }
    }) {
        Err(error) => {
            println!("{:?}", error);
        }
        Ok(_) => {}
    }

}
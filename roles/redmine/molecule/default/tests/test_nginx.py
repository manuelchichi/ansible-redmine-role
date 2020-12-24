def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled
    
def test_nginx_socket(host):
    socket = host.socket("tcp://0.0.0.0:80")
    assert socket.is_listening

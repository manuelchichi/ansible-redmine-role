def test_apache_is_installed(host):
    apache = host.package("apache2")
    assert apache.is_installed

def test_apache2_running_and_enabled(host):
    apache = host.service("apache2")
    assert apache.is_running
    assert apache.is_enabled
    
def test_apache2_socket(host):
    socket = host.socket("tcp://127.0.0.1:80")
    assert socket.is_listening

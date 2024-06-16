import docker
from hstest import StageTest, dynamic_test, CheckResult

test_network = "hyper-network"
test_volume = "hyper-volume"


class DockerTest(StageTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output = None
        self.client = docker.from_env()

    @dynamic_test()
    def test1(self):
        """Tests that network exists in the system"""
        network_names = "".join(network.attrs.get("Name") for network in self.client.networks.list())
        if test_network not in network_names:
            return CheckResult.wrong(f"'{test_network}' not found in the system networks!")

        return CheckResult.correct()

    @dynamic_test()
    def test2(self):
        """Tests that volume exists in the system"""
        volume_names = "".join(volume.attrs.get("Name") for volume in self.client.volumes.list())
        if test_volume not in volume_names:
            return CheckResult.wrong(f"'{test_volume}' not found in the system volumes!")

        return CheckResult.correct()


if __name__ == '__main__':
    DockerTest().run_tests()

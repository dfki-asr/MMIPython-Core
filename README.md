# MMIPython - Core

This repository contains the core implementation of MOSIM in Python 3. This includes the compiled thrift interfaces and data-model clases. To use this python integration, either directly install it with 

```console
pip install git@github.com:dfki-asr/MMIPython-Core.git
```

or clone or download this repository and install it directly with 

```console
pip install /path/to/your/MOSIM/download
```

For more information on the MOSIM repository, please visit our [main repository](https://github.com/dfki-asr/MOSIM) or the [MOSIM webpage](https://www.MOSIM.eu). 

## Package Structure

The MOSIM python package is structured in the following way: 
- `MOSIM.mmi`: auto-compiled thrift interface and data-model classes. Do not change these, as they will be overwritten when deploying a new MOSIM framework version
- `MOSIM.core`: base classes for MMUs, skeleton-access, scene-access and thrift clients
- `MOSIM.extensions`: helpful functions for handling MAvatarPostures, MQuaternions and MVector3s. 
- `MOSIM.abstraction`: Interface function definitions. 
- `MOSIM.adapter`: implementation of python-adapter functionality to handle python-MMUs
- `MOSIM.PythonAdapter`: implementation of a functional python adapter to host a set of MMUs

## Connecting to the MOSIM - Framework

If you want to connect to the Python, it is recommended to get the specific ports and addresses of individual services by accessing the MMI-Launcher. In the following example, we are assuming that the MMI-Launcher is running on the same machine (`127.0.0.1`) and on port (`9009`). 
For more information on the MMI-Launcher, check the documentation in the [main repository](https://github.com/dfki-asr/MOSIM) or the [thrift interface definition](https://github.com/dfki-asr/MOSIM). 

```python
RegisterClient = ThriftClient("127.0.0.1", 9009, MMIRegisterService.Client)
RegisterClient.__enter__()

session_id = RegisterClient._access.CreateSessionID({}) # create a new session
services = RegisterClient._access.GetRegisteredServices(session_id) # query the list of actives services. 
```

## Hosting Python MMUs 

If you developed a python MMU and want to connect it to the launcher, it is recommended to utilize the PythonAdapter. For an example of Python MMUs, please check the [Python Project Repository](https://github.com/dfki-asr/MOSIM-Python). 

```python 
import MOSIM.PythonAdapter as PythonAdapter
from path.to.my.mmu import MyMMU

description = ""
with open("path/to/my/description/", "r") as f:
	description = " ".join(f.readlines())

if __name__ == "__main__":
	list_of_mmus = [(description, MyMMU)]
	PythonAdapter.start_adapter(list_of_mmus)
```

By extending the `list_of_mmus`, multiple MMUs can be loaded by the same adapter. Hence, the python adapter is working fundamentally different than the C# and Unity adapters, which are loading MMUs from hard-drive via reflections. It was decided, to let the MMU developer decide which MMUs should run in the same adapter, as different MMUs can have fundamentally different requirements of the respective python environment. 

For MMU deployment, it is recommended to pack the complete environment, e.g. using Docker or [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html). To run the compiled Adapter, the Adapter can be either copied to Adapter folder, or in case of individual MMUs, to the MMU folder in addition with an `executable_description.json`, for example containing: 

```json
{
  "__isset": { "Dependencies": true },
  "Author": "Janis Sprenger, DFKI",
  "Dependencies": [],
  "ExecutableName": "MyMMU.exe",
  "ID": "my-unique-uuid",
  "Language": "Python",
  "Name": "MyMMU",
  "Version": "1.0"
}
```

## Contributing

If you would like to contribute code you can do so through GitHub by forking the repository and sending a pull request.

If you want to get involved more actively in the MOSIM project, please contact Janis Sprenger (DFKI) for further information.

## License

This project is licensed under the [MIT License](./LICENSE). 

Notice: Before you use the program in productive use, please take all necessary precautions, e.g. testing and verifying the program with regard to your specific use. The program was tested solely for our own use cases, which might differ from yours.

## Authors

As this project was merged from different git repositories, this list contains all additional authors, not tracked properly by github. 

- Jannes Lehwald (Daimler)
- Janis Sprenger (DFKI)
- Erik Herrmann (DFKI)
- Usama Bin Aslam (DFKI)
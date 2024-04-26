import sys

import Visualize

from gdpc import __url__, Editor
from gdpc.exceptions import InterfaceConnectionError, BuildAreaNotSetError

def run():
    editor = Editor()

    try:
        editor.checkConnection()
    except InterfaceConnectionError:
        print(
            f"Error: Could not connect to the GDMC HTTP interface at {editor.host}!\n"
            "To use GDPC, you need to use a \"backend\" that provides the GDMC HTTP interface.\n"
            "For example, by running Minecraft with the GDMC HTTP mod installed.\n"
            f"See {__url__}/README.md for more information."
        )
        sys.exit(1)

    try:
        buildArea = editor.getBuildArea()
    except BuildAreaNotSetError:
        print(
            "Error: failed to get the build area!\n"
            "Make sure to set the build area with the /setbuildarea command in-game.\n"
            "For example: /setbuildarea ~0 0 ~0 ~64 200 ~64"
        )
        sys.exit(1)

    if buildArea.size.x > 300 | buildArea.size.z > 300:
        print("The build area is too large, try a size smaller than 300 in the x and z axis.")
        sys.exit(1)

    Visualize.visualize()


if __name__ == '__main__':
    run()

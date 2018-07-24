# alt

[![Build Status](https://travis-ci.org/dotboris/alt.svg?branch=master)](https://travis-ci.org/dotboris/alt)

Tool for switching between different versions of commands.

## Installation

Currently, `alt` doesn't have a binary release. If you want to use `alt`, you'll
need to build it from source.

1.  Setup a rust development environment

    See: https://doc.rust-lang.org/book/second-edition/ch01-01-installation.html

1.  Clone this repository

    ```sh
    git clone https://github.com/dotboris/alt.git
    cd alt
    ```

1.  Build & Install `alt` from source

    ```sh
    cargo install
    ```

1.  Check if `alt` is available

    ```sh
    alt --help
    ```

1.  Add the shims directory to your `PATH` environment variable

    ```sh
    # in ~/.zshrc or ~/.bashrc
    export PATH="$HOME/.local/alt/shims:$PATH"
    ```

## Usage

In order to use `alt`, there are two things that you need to do:

1.  Tell `alt` about the commands on your system and their different versions
1.  Tell `alt` what version of a given command you want to use in a directory

### Defining commands and versions

#### Automatic scanning

`alt` can automatically scan your system to find different versions of command.

```sh
alt scan some-command
```

Currently, scanning supports:

- Looking through `PATH` for commands with version suffixes

#### Manual definition

`alt` looks for commands and their versions in the `~/.config/alt/defs.toml`
file. Open that file with your text editor of choice.
(create it if it's not already there)

Here's an example of a command definition file:

```toml
# A section defines a command
# Here we define the python command
[python]
# Under a section we associate a version name (in this case 2 and 3) to executable.
# You can name versions whatever you want. We use version numbers because it's simple
2 = "/usr/bin/python2"
3 = "/usr/bin/python3"

# Another section defining the node command
[node]
4 = "/path/to/node4/bin/node"
6 = "/path/to/node6/bin/node"
8 = "/path/to/node8/bin/node"
```

When you make changes to the command definitions, remember to generate the shims.

```sh
alt shim
```

### Switching command versions

`alt` uses the directory you're currently in to figure out which versions of
commands to run. When switching versions, everything is related to the current
directory.

```sh
cd directory/of/interest
alt use some-command
```

## Development

TODO: development doc

## Relase

1.  Update version in `Cargo.toml`
1.  Update `Cargo.lock`

    ```sh
    cargo build
    ```

1.  Commit your version bump

    ```sh
    git add .
    git commit -m 'bump version to v{your version number}'
    ```

1.  Tag a new version

    ```sh
    git tag v{your-version-number}
    ```

1.  Push everything

    ```sh
    git push --tags origin master
    ```

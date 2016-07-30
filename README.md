# ci-dice

## About
A console dice roll application, useful in simulating CI passes and failures.

While this is maintained by the Ubuntu OpenStack Engineering Team, it is not
specific to OpenStack use cases.  Any CI pipeline can use ci-dice as a way
to simulate, confirm and/or debug the pipeline's behaviour.


## Usage
While this tool can be run from a fresh git clone of the repo, a more
interesting and convenient way to consume it is via snaps.

```
snap install ci-dice
```

## Files in Repo
* ci-dice:
    * The main executable.  It runs ci_dice.py, but can optionally be linked
      to the bash version if desired.
* ci_dice.py:
    * A simple tool to randomly pass or fail.  It is useful as a command or
      module in a CI job to simulate, debug or build out CI pipelines.
    * Defaults to 2 dice, fail if a match is rolled (~16.6% probability).
    * TODO: Expose the dice quantity, logic/odds inversion and other 
      configuraton as cli parameters.
* ci_dice.sh:
    * A legacy version of the python3 rewrite above.
    * A simple tool to randomly pass or fail.  It is useful as a
      command or module to simulate, debug or build out CI pipelines. Seeds
      with PID.  Rolls a pair of dice.  Fails if the pair matches.
      ~16.666% probability.  No invert logic or dice quantity options.

## Snacking (snap hacking)
The ci-dice repo contains the necessary bits to use snapcraft to build
a snap package.  The snapd and snapcraft tools are available on Ubuntu 16.04
and later (with support for 14.04 underway).

### Example

```
# Ensure the right tools are present
apt-get install snapcraft snapd
git clone <the ci-dice repo>
cd <the ci-dice checkout dir>
# Edit, hack, edit, edit.

# Build the new snap
snapcraft
```

### Testing

Execute lint checks.
```
sudo apt-get install tox
tox
```

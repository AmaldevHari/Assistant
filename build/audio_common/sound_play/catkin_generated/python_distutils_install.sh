#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/amaldev/Assistant/src/audio_common/sound_play"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/amaldev/Assistant/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/amaldev/Assistant/install/lib/python2.7/dist-packages:/home/amaldev/Assistant/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/amaldev/Assistant/build" \
    "/usr/bin/python2" \
    "/home/amaldev/Assistant/src/audio_common/sound_play/setup.py" \
    egg_info --egg-base /home/amaldev/Assistant/build/audio_common/sound_play \
    build --build-base "/home/amaldev/Assistant/build/audio_common/sound_play" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/amaldev/Assistant/install" --install-scripts="/home/amaldev/Assistant/install/bin"

# TBS Robotics RMRC 2022 Source Code and Setup
TBS Robotics RMRC 2022 Source Code and Setup
## Prepare robot and control station
- Wireless access point
- Connect to network
- Connect gamepad
- Connect battery packs
## Robot (JETSON Nano) source code and setup
- `dxl_4x_drive.py`
- `gst_stream_udp_0.sh`
- `TBS_4x_PS4_TCP_v1.py`
## Control station (laptop) source code and setup
- `pyDS4_controller_pickle_v4.py`
- `gstream_udp_player_1.sh`
- `send_motor_speed_v1.py`
## Start up sequence
- From control station, open two `ssh -x user@IP` terminals to JETSON. Open two local terminals at control station.
- Following is a recommended sequence to run codes
- Run motor codes for the first time run
  - Control station: `python3 pyDS4_controller_pickle_v4.py &`
  - JETSON: `python3 TBS_4x_PS4_TCP_v1.py`
  - Control station: `python3 send_motor_speed_v1.py`
- Run camera streaming
  - Control station: `./gstream_udp_player_1.sh`
  - JETSON: `./gst_stream_udp_0.sh`
- `python3 pyDS4_controller_pickle_v4.py &` run as a background process. You will need to kill it to restart the whole robot. Run `ps` to find out process number for this program, then `kill xxxx`, where `xxxx` is the process number.
- After the first time run, pickle in `pyDS4_controller_pickle_v4.py` should have save the `motorspeed.ps4`. And the file exist for `send_motor_speed_v1.py`. Otherwise it will stop with an error that it cannot find `motorspeed.ps4`. After initial run, you can utilize a set of scripts to run the robot.
- Enjoy your drive!

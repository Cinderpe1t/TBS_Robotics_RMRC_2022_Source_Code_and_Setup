# TBS Robotics RMRC 2022 Source Code and Setup
TBS Robotics RMRC 2022 Source Code and Setup
## Prepare robot
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
## Prepare remote access
- From control station, open two `ssh -x user@IP` terminals
- Following is a recommended sequence to run codes
- Motor codes for the first time run
  - Control station: `python3 pyDS4_controller_pickle_v4.py`
  - JETSON: `python3 TBS_4x_PS4_TCP_v1.py`
  - Control station: `python3 send_motor_speed_v1.py`
- Camera codes
  - Control station: `./gstream_udp_player_1.sh`
  - JETSON: `./gst_stream_udp_0.sh`
- Enjoy your drive!

import numpy as np
import matplotlib.pyplot as plt
import math

sim_time=100
m=1.034
c=-36

desired_pitch_pid = np.loadtxt('desired_pitch_pid')
desired_yaw_pid = np.loadtxt('desired_yaw_pid')
solution_matrix_pid = np.loadtxt('solution_matrix_pid')
solution_time_pid = np.loadtxt('solution_time_pid')

desired_pitch_lqr = np.loadtxt('desired_pitch_lqr')
desired_yaw_lqr = np.loadtxt('desired_yaw_lqr')
solution_matrix_lqr = np.loadtxt('solution_matrix_lqr')
solution_time_lqr = np.loadtxt('solution_time_lqr')

length = desired_pitch_pid.shape[0]
time = np.linspace(0,sim_time,num=length,endpoint=True)

length_lqr = desired_pitch_lqr.shape[0]
time_lqr = np.linspace(0,sim_time,num=length_lqr,endpoint=True)

x_pid = solution_matrix_pid[0,:]
y_pid = solution_matrix_pid[1,:]
z_pid = solution_matrix_pid[2,:]
roll_pid = solution_matrix_pid[3,:]*180/math.pi
pitch_pid = solution_matrix_pid[4,:]*180/math.pi
yaw_pid = solution_matrix_pid[5,:]*180/math.pi

x_lqr = solution_matrix_lqr[0,:]
y_lqr = solution_matrix_lqr[1,:]
z_lqr = solution_matrix_lqr[2,:]
roll_lqr = solution_matrix_lqr[3,:]*180/math.pi
pitch_lqr = solution_matrix_lqr[4,:]*180/math.pi
yaw_lqr = solution_matrix_lqr[5,:]*180/math.pi

desired_z = np.linspace(30,30,num=length,endpoint=True)
desired_z_lqr = np.linspace(30,30,num=length_lqr,endpoint=True)

desired_x = np.linspace(min(min(x_pid),min(x_lqr)),max(max(x_pid),max(x_lqr)),num=10,endpoint=True)
desired_y = m*desired_x + c

plt.figure(figsize=(5, 4)) 

# plt.subplot(2, 2, 1) 
# plt.plot(solution_time_pid,z_pid,'b',label='Present z PID')
# plt.plot(time,desired_z,'--k',label='Desired z')
# plt.plot(solution_time_lqr,z_lqr,'r',label='Present z LQR')
# plt.ylabel('Z (m)')
# plt.xlabel('Time (sec)')
# plt.title('Z vs time')
# plt.legend()
# plt.grid()

# plt.subplot(2, 2, 2)
# plt.plot(solution_time_pid,pitch_pid,'b',label='Present pitch PID')
# plt.plot(time,desired_pitch_pid,'b--',label='Desired pitch PID')
# plt.plot(solution_time_lqr,pitch_lqr,'r',label='Present pitch LQR')
# plt.plot(time_lqr,desired_pitch_lqr,'r--',label='Desired pitch LQR')
# plt.ylabel('Pitch angle (degrees)')
# plt.xlabel('Time (sec)')
# plt.legend()
# plt.title('Pitch vs time')
# plt.grid()

# plt.subplot(2, 2, 3)
# plt.plot(solution_time_pid,yaw_pid,'b',label='Present yaw PID')
# plt.plot(time,desired_yaw_pid,'b--',label='Desired yaw PID')
# plt.plot(solution_time_lqr,yaw_lqr,'r',label='Present yaw LQR')
# plt.plot(time_lqr,desired_yaw_lqr,'r--',label='Desired yaw LQR')
# plt.ylabel('Yaw angle (degrees)')
# plt.xlabel('Time (sec)')
# plt.title('Yaw vs time')
# plt.legend()
# plt.grid()

# plt.subplot(2, 2, 4)
# plt.plot(x_pid,y_pid,'b',label='AUV motion PID ')
# plt.plot(x_lqr,y_lqr,'r',label='AUV motion LQR')
# plt.plot(desired_x,desired_y,'--k',label='Desired motion')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.title('X vs Y')
# plt.grid()

plt.plot(solution_time_pid,roll_pid,'b',label='Present roll PID')
plt.plot(solution_time_lqr,roll_lqr,'g',label='Present roll LQR')
plt.ylabel('Roll angle (degrees)')
plt.xlabel('Time (sec)')
plt.legend()
plt.title('Roll vs time')
plt.grid()
 
plt.show()
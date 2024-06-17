import numpy as np
import matplotlib.pyplot as plt
import math

sim_time=100
m=1.034
c=-34


solution_matrix_pid = np.loadtxt('solution_matrix_pid')
solution_time_pid = np.loadtxt('solution_time_pid')

solution_matrix_lqr = np.loadtxt('solution_matrix_lqr')
solution_time_lqr = np.loadtxt('solution_time_lqr')


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

desired_pitch = np.linspace(0,0,num=solution_time_lqr.shape[0],endpoint=True)
desired_yaw = np.linspace(math.atan(m)*180/math.pi,math.atan(m)*180/math.pi,num=solution_time_lqr.shape[0],endpoint=True)
desired_z = np.linspace(30,30,num=solution_time_lqr.shape[0],endpoint=True)
desired_x =  np.linspace(min(min(x_pid),min(x_lqr)),max(max(x_pid),max(x_lqr)),num=10,endpoint=True)
desired_y = m*desired_x + c

plt.figure(figsize=(5, 4)) 

# plt.subplot(2, 2, 1) 
# plt.plot(solution_time_pid,z_pid,'b',label='Present z PID')
# plt.plot(solution_time_lqr,desired_z,'--k',label='Desired z')
# plt.plot(solution_time_lqr,z_lqr,'r',label='Present z LQR')
# plt.ylabel('Z (m)')
# plt.xlabel('Time (sec)')
# plt.title('Z vs time')
# plt.legend()
# plt.grid()

# plt.subplot(2, 2, 2)
# plt.plot(solution_time_pid,pitch_pid,'b',label='Present pitch PID')
# plt.plot(solution_time_lqr,desired_pitch,'--k',label='Desired pitch')
# plt.plot(solution_time_lqr,pitch_lqr,'r',label='Present pitch LQR')
# plt.legend()
# plt.ylabel('Pitch angle (degrees)')
# plt.xlabel('Time (sec)')
# plt.title('Pitch vs time')
# plt.grid()

# plt.subplot(2, 2, 3)
# plt.plot(solution_time_pid,yaw_pid,'b',label='Present yaw PID')
# plt.plot(solution_time_lqr,desired_yaw,'--k',label='Desired yaw')
# plt.plot(solution_time_lqr,yaw_lqr,'r',label='Present yaw LQR')
# plt.ylabel('Yaw angle (degrees)')
# plt.xlabel('Time (sec)')
# plt.title('Yaw vs time')
# plt.legend()
# plt.grid()

# plt.subplot(2, 2, 4)
# plt.plot(x_pid,y_pid,'b',label='AUV motion PID ')
# plt.plot(x_lqr,y_lqr,'r',label='AUV motion LQR')
# plt.plot(desired_x,desired_y,'--k',label='Desired motion')
# plt.xlabel('X (m)')
# plt.ylabel('Y (m)')
# plt.legend()
# plt.title('X vs Y')
# plt.grid()


# plt.suptitle('Comparison plot')  

plt.plot(solution_time_pid,roll_pid,'r',label='Roll PID')
plt.plot(solution_time_lqr,roll_lqr,'--k',label='Roll LQR')
plt.ylabel('Roll (degrees)')
plt.xlabel('Time (sec)')
plt.title('Roll vs time')
plt.legend()
plt.grid()

plt.show()
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def questions():
    #Receiveing the user's input
    print("Laten we Willy een dansje doen!")
    speed = input("Snelheid:")
    distance = input("Afstand:")
    isForward = input("Vooruit?: ")#True or False

def move():
    # Starts a new node
    rospy.init_node('move_willy', anonymous=True)
    velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    #Receiveing the user's input
    #print("Laten we Willy een dansje doen!")
    #speed = input("Snelheid:")
    #distance = input("Afstand:")
    #isForward = input("Vooruit?: ")#True or False
    
    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    
    #if(isTurnLeft):
    #    vel_msg.linear.z = abs(speed)
    
    #Since we are moving just in x-axis
    #vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)


        

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
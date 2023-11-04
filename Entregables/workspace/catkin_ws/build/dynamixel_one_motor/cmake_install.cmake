# Install script for directory: /home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/src/dynamixel_one_motor

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/figuras/pose1.png;/figuras/pose2.png;/figuras/pose3.png;/figuras/pose4.png;/figuras/poshome.png;/figuras/def.png")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/figuras" TYPE FILE FILES
    "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/src/dynamixel_one_motor/src/dynamixel_one_motor/figuras/pose1.png"
    "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/src/dynamixel_one_motor/src/dynamixel_one_motor/figuras/pose2.png"
    "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/src/dynamixel_one_motor/src/dynamixel_one_motor/figuras/pose3.png"
    "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/src/dynamixel_one_motor/src/dynamixel_one_motor/figuras/pose4.png"
    "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/src/dynamixel_one_motor/src/dynamixel_one_motor/figuras/poshome.png"
    "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/src/dynamixel_one_motor/src/dynamixel_one_motor/figuras/def.png"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/build/dynamixel_one_motor/catkin_generated/installspace/dynamixel_one_motor.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamixel_one_motor/cmake" TYPE FILE FILES
    "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/build/dynamixel_one_motor/catkin_generated/installspace/dynamixel_one_motorConfig.cmake"
    "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/build/dynamixel_one_motor/catkin_generated/installspace/dynamixel_one_motorConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamixel_one_motor" TYPE FILE FILES "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/src/dynamixel_one_motor/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/dynamixel_one_motor" TYPE PROGRAM FILES "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/build/dynamixel_one_motor/catkin_generated/installspace/jointSrv.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/dynamixel_one_motor" TYPE PROGRAM FILES "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/build/dynamixel_one_motor/catkin_generated/installspace/jointSub.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/dynamixel_one_motor" TYPE PROGRAM FILES "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/build/dynamixel_one_motor/catkin_generated/installspace/jointPub.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/dynamixel_one_motor" TYPE PROGRAM FILES "/home/gio/Unal/Robot/lab4/lab4/Entregables/workspace/catkin_ws/build/dynamixel_one_motor/catkin_generated/installspace/phantomHMI.py")
endif()


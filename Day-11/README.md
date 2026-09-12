# Day 11 – ROS 2 Python Package

## Objective

To understand the structure and working of a ROS 2 Python package and create a small Python package containing Publisher and Subscriber nodes.

---

## 1. Introduction

A ROS 2 Python package provides an organized structure for developing Python-based ROS 2 applications.

In this practical, an `ament_python` package named `day11_python_package` was created. The package contains a Publisher node and a Subscriber node that communicate using a ROS 2 topic.

---

## 2. Package Structure

```text
Day-11/
├── ros2_ws/
│   └── src/
│       └── day11_python_package/
│           ├── day11_python_package/
│           │   ├── __init__.py
│           │   ├── publisher.py
│           │   └── subscriber.py
│           ├── resource/
│           │   └── day11_python_package
│           ├── test/
│           ├── package.xml
│           ├── setup.py
│           └── setup.cfg
└── screenshots/

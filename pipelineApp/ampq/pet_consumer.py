#!/usr/bin/env python
from worker import Worker
import sys, os

workerInsert = Worker('pet')

workerInsert.consume()
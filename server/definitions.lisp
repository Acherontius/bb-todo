(defpackage #:bb-todo
  (:use #:cl))

(in-package #:bb-todo)

(defclass project ()
  ((name :initarg :name :accessor project-name)
   (client :initarg :client :accessor project-client)))

(defclass task ()
  ((title :initarg :title :accessor task-title)
   (description :initarg :description :accessor task-description)
   (due-date :initarg :due-date :accessor task-due-date)
   (project :initarg :project :accessor task-project :type project)
   (priority :initarg :priority :accessor task-priority))) ;'high 'medium 'low

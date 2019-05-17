Feature: Checking RemoveDirAndFile creation and working

  #1
  Scenario: Checking RemoveDirAndFile creation
     Given I have class RemoveDirAndFile
      When I create new class RemoveDirAndFile
      Then I have created RemoveDirAndFile

#2
  Scenario: Checking remove file
     Given I have a file with a path <file_path>
      When I call method with param <file_path> which remove file
      Then File with a path <file_path> was remove
      
#3
  Scenario: Checking remove dir
     Given I have a dir with a path <dir_path>
      When I call method with param <dir_path> which remove dir
      Then Dir with a path <dir_path> was remove
       
#4
  Scenario: Checking fill file
     Given I have a file with a path <file_path>
      When I call method with param <file_path> which write <data> to file
      Then File with a path <file_path> was filled with <data>

#5
  Scenario: Checking exist file
     Given I have a file with a path <file_path>
      When I call method with param <file_path> which check exist file or dir
      Then File or dir with a path <file_path> exist
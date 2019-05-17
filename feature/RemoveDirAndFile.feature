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

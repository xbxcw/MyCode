# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2018.3.4\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2018.3.4\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\HYC\Documents\MyCode\clion

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\HYC\Documents\MyCode\clion\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/clion.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/clion.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/clion.dir/flags.make

CMakeFiles/clion.dir/main.cpp.obj: CMakeFiles/clion.dir/flags.make
CMakeFiles/clion.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\HYC\Documents\MyCode\clion\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/clion.dir/main.cpp.obj"
	C:\PROGRA~1\mingw64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\clion.dir\main.cpp.obj -c C:\Users\HYC\Documents\MyCode\clion\main.cpp

CMakeFiles/clion.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/clion.dir/main.cpp.i"
	C:\PROGRA~1\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\HYC\Documents\MyCode\clion\main.cpp > CMakeFiles\clion.dir\main.cpp.i

CMakeFiles/clion.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/clion.dir/main.cpp.s"
	C:\PROGRA~1\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\HYC\Documents\MyCode\clion\main.cpp -o CMakeFiles\clion.dir\main.cpp.s

CMakeFiles/clion.dir/Enemy.cpp.obj: CMakeFiles/clion.dir/flags.make
CMakeFiles/clion.dir/Enemy.cpp.obj: ../Enemy.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\HYC\Documents\MyCode\clion\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/clion.dir/Enemy.cpp.obj"
	C:\PROGRA~1\mingw64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\clion.dir\Enemy.cpp.obj -c C:\Users\HYC\Documents\MyCode\clion\Enemy.cpp

CMakeFiles/clion.dir/Enemy.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/clion.dir/Enemy.cpp.i"
	C:\PROGRA~1\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\HYC\Documents\MyCode\clion\Enemy.cpp > CMakeFiles\clion.dir\Enemy.cpp.i

CMakeFiles/clion.dir/Enemy.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/clion.dir/Enemy.cpp.s"
	C:\PROGRA~1\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\HYC\Documents\MyCode\clion\Enemy.cpp -o CMakeFiles\clion.dir\Enemy.cpp.s

# Object files for target clion
clion_OBJECTS = \
"CMakeFiles/clion.dir/main.cpp.obj" \
"CMakeFiles/clion.dir/Enemy.cpp.obj"

# External object files for target clion
clion_EXTERNAL_OBJECTS =

clion.exe: CMakeFiles/clion.dir/main.cpp.obj
clion.exe: CMakeFiles/clion.dir/Enemy.cpp.obj
clion.exe: CMakeFiles/clion.dir/build.make
clion.exe: CMakeFiles/clion.dir/linklibs.rsp
clion.exe: CMakeFiles/clion.dir/objects1.rsp
clion.exe: CMakeFiles/clion.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\HYC\Documents\MyCode\clion\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable clion.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\clion.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/clion.dir/build: clion.exe

.PHONY : CMakeFiles/clion.dir/build

CMakeFiles/clion.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\clion.dir\cmake_clean.cmake
.PHONY : CMakeFiles/clion.dir/clean

CMakeFiles/clion.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\HYC\Documents\MyCode\clion C:\Users\HYC\Documents\MyCode\clion C:\Users\HYC\Documents\MyCode\clion\cmake-build-debug C:\Users\HYC\Documents\MyCode\clion\cmake-build-debug C:\Users\HYC\Documents\MyCode\clion\cmake-build-debug\CMakeFiles\clion.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/clion.dir/depend


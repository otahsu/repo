cmake_minimum_required(VERSION 2.8)

project(proj1)
set(SRCS main.c)
add_executable(proj1 ${SRCS})
add_subdirectory(module1)
target_link_libraries(proj1 mod1)

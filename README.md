# UVM (Universal Verification Methodology)

## 1. [Introduction to Verification and UVM](UVM_Examples/1__Introduction.md)
   - Definition of Verification
   - Verification Challenges
   - Introduction to Universal Verification Methodology (UVM)
   - Advantages of UVM

## 2. [Object-Oriented Programming (OOP) Basics (Review)](UVM_Examples/2__OOP_Basics.md)
   - Classes and Objects
   - Inheritance
   - Polymorphism
   - Encapsulation

## 3. [UVM Architecture and Components](UVM_Examples/3__Architecture.md)
   - Structure of a UVM Testbench
   - UVM Components:
     - Test
     - Testbench
     - Environment
     - Agent
     - Driver
     - Monitor
     - Sequencer
     - Scoreboard

## 4. [UVM Phases and Sequences](UVM_Examples/4__Phases_Sequences.md)
   - Phases in UVM:
     - Build
     - Connect
     - Run
     - Report
     - Final
   - Sequences in UVM:
     - Creating Sequences
     - Configuring Sequences
     - Sequencer-Sequence Communication

## 5. [Transactions and TLM (Transaction-Level Modeling)](UVM_Examples/5__TLM.md)
   - Transaction Class
   - TLM Ports and Exports
   - TLM Communication: Blocking vs. Non-Blocking

## 6. [UVM Configuration](UVM_Examples/6__Configurations.md)
   - Configuration Objects
   - Configuration Database
   - Using the `uvm_config_db`

## 7. [UVM RAL (Register Abstraction Layer)](UVM_Examples/7__RAL.md)
   - Introduction to RAL
   - RAL Model Creation
   - Register Access Mechanisms
   - Register Sequences

## 8. [UVM Messaging and Reporting](UVM_Examples/8__Messaging.md)
   - Message Macros
   - Message Verbosity Levels
   - Customizing Messages

## 9. [UVM Phasing and Sequencing Macros](UVM_Examples/9__Phasing_Sequencing_Macros.md)
   - `uvm_phase`
   - `uvm_sequence`
   - `uvm_do_with`
   - `uvm_do`

## 10. [UVM Testbench Automation](UVM_Examples/10__Testbench_Automation.md)
   - Using `run_test()` Function
   - Configuration Automation
   - Testbench Automation Guidelines

## 11. [Tips and Best Practices](UVM_Examples/11__Best_Practices.md)
   - Coding Guidelines
   - Debugging Techniques
   - Performance Optimization

## 12. [Case Study: Building a UVM Testbench](UVM_Examples/12__Case_Study.md)
   - Step-by-step construction of a UVM testbench for a simple design
   - Testbench components interconnection
   - Sequences and transactions usage
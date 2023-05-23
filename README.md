# BIGD_GarbageCollection

BIGD_GarbageCollection
가비지 컬렉션(Garbage Collection) - GC

시스템에서 더이상 사용하지 않는 동적 할당된 메모리 블럭을 찾아 자동으로 다시 사용 가능한 자원으로 회수하는 메모리 관리 방법
필요한 이유

메모리 누수를 방지하고 메모리 관리를 자동화하여 개발자가 명시적으로 메모리를 해제하는 번거로움을 줄이기 위해 사용됩니다.
더 이상 참조되지 않고 쓰이지 않는 객체들이 메모를 잡아 먹는 것을 줄여주기 위해서 직접 삭제를 명시해야할 필요를 줄이기 위해 사용
동작 순서

객체 추적
가비지 식별
메모리 해제
동작 방식

Stop The World - 실행중인 작업을 멈추고 필요없는 메모리를 찾아서 삭제하는 방식 빠르게 GC를 수행하지만 그 시간 동안에는 쓰레드가 멈춰 다른 애플리케이션이 중단되는 문제가 있음

Mark and Sweep - 사용 되고 있는 메모리를 체크하여 Mark하고 Mark가 되어 있지 않는 객체들을 메모리에서 제거하는 과정(Sweep)

참조 :

https://blog.metafor.kr/163

https://mangkyu.tistory.com/118

https://ko.javascript.info/garbage-collection

chatGPT

import pytest
import hashlib


def test_1():
    import module_1 as m1
    if 'd' in dir(m1):
        h = hashlib.sha256(m1.d.to_bytes(10, 'little')).hexdigest()
        assert  h == '90eff099fceac903cc19459372565bd49c567aa5c3fcaef62eacd3a3e52f1f77'
    else:
        assert False


def test_2():
    import module_2 as m2
    if  {'i', 'f', 's', 'b'}.issubset(set(dir(m2))):
        h = hashlib.sha256("{},{},{},{}".format(type(m2.i), type(m2.f), type(m2.s), type(m2.b)).encode('utf-8')).hexdigest()
        assert  h == '87e913e1e12ff7c35ed289bcc7c5951d9b356ea123b28075179eac44a7dfdd5d'
    else:
        assert False


def test_3():
    import module_3 as m3
    if  'a' in dir(m3):
        h = hashlib.sha256(int(m3.a).to_bytes(10, 'little')).hexdigest()
        assert  h == '87a6e9757d3898202648bc17aed200539214ffc88cce9825b06f9f48fddcc876'
    else:
        assert False


def test_4():
    import module_4 as m4
    if  'greeting' in dir(m4):
        assert m4.greeting == 'Hello, {ksdj}!'.format(ksdj=m4.name)
    else:
        assert False


def test_5():
    import module_5 as m5
    if 'part' in dir(m5):
        h = hashlib.sha256(m5.part.encode('utf-8')).hexdigest()
        assert  h == 'ab2620f9b7154d9f9dc1b3c2d949d85d595fe77f45411b3dbe6e5b47da564177'
    else:
        assert False


def test_6():
    import module_6 as m6
    if 'all_uni' in dir(m6):
        h = hashlib.sha256(m6.all_uni.to_bytes(10, 'little')).hexdigest()
        assert  h == '77a92b9998621186a135c91699ab6e77466dfaea5d10bc679c860ca9cd7cf415'
    else:
        assert False


def test_7():
    import module_7 as m7
    if 'split_list' in dir(m7):
        l = b'Y\x15\x1f\x15;\x0cA0 &#\x12`9\x0b\tK+U6AF\x17C\x1b\x0bD`D\x05&.K34a:U@;\x1f_FKA\x0b0"F\x1f'
        low, high = m7.split_list(l, 51)
        if min(high) >= 51 and max(low) < 51:
            assert True
        else:
            assert False
    else:
        assert False


def test_8():
    assert False

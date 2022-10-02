import { useAppSelector, useAppDispatch } from '../../app/hooks';
import React, { useEffect, useRef, useState } from 'react';
import { Input, Tag, Tooltip } from 'antd';
import type { InputRef } from 'antd';
import axios from 'axios';
import { PlusOutlined } from '@ant-design/icons';
export default function ConfigDomains () {
    const dispatch = useAppDispatch();
    
    // const domains = useAppSelector((state) => state.configSettings.domains);
    const [tags, setTags] = useState<string[]>([]);
    const [inputVisible, setInputVisible] = useState(false);
    const [inputValue, setInputValue] = useState('');
    const [editInputIndex, setEditInputIndex] = useState(-1);
    const [editInputValue, setEditInputValue] = useState('');
    const inputRef = useRef<InputRef>(null);
    const editInputRef = useRef<InputRef>(null);
    
    useEffect(() => {
        axios.get("http://10.8.0.4:7000/api/config/get").then((response) => {
            if(response.data.data.domain !== undefined) {
                setTags(response.data.data.domain);
            }
        });
    }, []);

    useEffect(() => {
        if (inputVisible) {
          inputRef.current?.focus();
        }
      }, [inputVisible]);
    
    useEffect(() => {
        editInputRef.current?.focus();
    }, [inputValue]);

    const handleClose = (removedTag: string) => {
        const newTags = tags.filter(tag => tag !== removedTag);
        axios.post("http://10.8.0.4:7000/api/config/domain/add", newTags);
        console.log(newTags);
        setTags(newTags);
    };

    const showInput = () => {
        setInputVisible(true);
    };


    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setInputValue(e.target.value);
    };

    const handleInputConfirm = () => {
        if (inputValue && tags.indexOf(inputValue) === -1) {
          setTags([...tags, inputValue]);
          axios.post("http://10.8.0.4:7000/api/config/domain/add", [...tags, inputValue]);
        }
        setInputVisible(false);
        setInputValue('');
    };

    const handleEditInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setEditInputValue(e.target.value);
    };

    const handleEditInputConfirm = () => {
        const newTags = [...tags];
        newTags[editInputIndex] = editInputValue;
        setTags(newTags);
        setEditInputIndex(-1);
        setInputValue('');
        console.log("running");
        axios.post("http://10.8.0.4:7000/api/config/domain/add", [...tags, inputValue]);
    };
    // useEffect(() => {
    //     // dispatch(setConfigSettings(response.data));
    //     let tempTags:any[] = [];
    //     console.log(domains);
    //     domains.forEach((domain) => {
    //         tempTags.push(<Tag closable onClose={handleOnClick}>
    //             {domain}
    //           </Tag>);
    //     });
    //     setTags(tempTags);
    // }, []);
    return (<>
        <div style={{ fontSize: '25px' }}>Tracked Domains</div>
        {tags.map((tag, index) => {
        if (editInputIndex === index) {
          return (
            <Input
              ref={editInputRef}
              key={tag}
              size="small"
              className="tag-input"
              value={editInputValue}
              onChange={handleEditInputChange}
              onBlur={handleEditInputConfirm}
              onPressEnter={handleEditInputConfirm}
            />
          );
        }
        const isLongTag = tag.length > 20;

        const tagElem = (
          <Tag
            color='blue'
            className="edit-tag"
            key={tag}
            closable={true}
            onClose={() => handleClose(tag)}
          >
            <span
              onDoubleClick={e => {
                if (index !== 0) {
                  setEditInputIndex(index);
                  setEditInputValue(tag);
                  e.preventDefault();
                }
              }}
            >
              {isLongTag ? `${tag.slice(0, 20)}...` : tag}
            </span>
          </Tag>
        );
        return isLongTag ? (
          <Tooltip title={tag} key={tag}>
            {tagElem}
          </Tooltip>
        ) : (
          tagElem
        );
      })}
      {inputVisible && (
        <Input
          ref={inputRef}
          type="text"
          size="small"
          className="tag-input"
          value={inputValue}
          onChange={handleInputChange}
          onBlur={handleInputConfirm}
          onPressEnter={handleInputConfirm}
        />
      )}
      {!inputVisible && (
        <Tag className="site-tag-plus" onClick={showInput}>
          <PlusOutlined /> New Tag
        </Tag>
      )}
    </>);
}
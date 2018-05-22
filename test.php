<?php
/**
 * User: Tingting GE
 * Date: 17/1/5
 */
class Car_Commonlib_Data_AdminRecords extends aaa
{
    private $daoRecords;
    public function __construct()
    {
        $this->daoRecords = new Car_Commonlib_Dao_AdminRecords();
    }
    /**
     * @param $action
     * @param $controller
     * @return 成功
     */
     function addRecord($action, $controller, $request)
    {
        $operator = Car_Commonlib_Utils_AuthUtility::getUserName(null, Car_Commonlib_Utils_AuthUtility::AUTH_UUAP);
        return $this->daoRecords->addRecord($operator, $action, $controller, $request);
    }
    /**
     * @param null $beginTime
     * @param null $endTime
     * @param null $operator
     * @param null $action
     * @param null $controller
     * @param int $offset
     * @param int $limit
     * @return array|成功
     * @throws Car_Commonlib_Exception_Usability
     */
    public function getRecords($beginTime = null, $endTime = null, $operator = null,
                               $action = null, $controller = null, $offset = 0, $limit = 20)
    {
        if (empty($endTime)) {
            $endTime = time();
        }
        if ($beginTime > $endTime) {
            throw new Car_Commonlib_Exception_Usability('begin time is larger than endtime.',
                Car_Commonlib_Constants_ErrorCodes::INVALID_PARAM);
        }
        return $this->daoRecords->getRecords($beginTime, $endTime, $operator, $action, $controller,
            $offset, $limit);
    }
}    $EXT->call_hook('post_system');